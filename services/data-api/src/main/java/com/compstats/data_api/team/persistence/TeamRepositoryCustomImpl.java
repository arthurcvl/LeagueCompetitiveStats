package com.compstats.data_api.team.persistence;

import com.compstats.data_api.team.enums.ComparisonType;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import jakarta.persistence.TypedQuery;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class TeamRepositoryCustomImpl implements TeamRepositoryCustom {

    @PersistenceContext
    private EntityManager entityManager;

    private List<String> expectedValues = new ArrayList<>(List.of("kills", "dragons", "towers", "matchDuration"));

    @Override
    public Double getAverageByTeamNameStatus(String teamName, String statusName) {

        if(!expectedValues.contains(statusName)){
            throw new IllegalArgumentException("");
        }

        String jpql = "SELECT ROUND(AVG(" + statusName + "), 2) FROM Team a WHERE a.teamName = :teamNameParam";

        TypedQuery<Double> query = entityManager.createQuery(jpql, Double.class);
        query.setParameter("teamNameParam", teamName);
        return query.getSingleResult();
    }

    @Override
    public Double getRelativeFrequencyByTeamNameStatus(String teamName, String statusName, Integer mark, ComparisonType comparisonType) {
        String comparisonSignal;
        if(comparisonType.equals(ComparisonType.GREATER)){
            comparisonSignal = ">";
        } else {
            comparisonSignal = "<";
        }

        if(isMarkNotValidValue(mark)){
            throw new IllegalArgumentException();
        }

        if(!expectedValues.contains(statusName)){
            throw new IllegalArgumentException("");
        }

        String jpql = "SELECT CAST((SELECT COUNT(*) FROM Team a WHERE " + statusName + " " + comparisonSignal + " :mark AND a.teamName = :teamNameParam) AS DOUBLE)" + " / (SELECT COUNT(*) FROM Team a WHERE a.teamName = :teamNameParam)";

        TypedQuery<Double> query = entityManager.createQuery(jpql, Double.class);
        query.setParameter("mark", mark);
        query.setParameter("teamNameParam", teamName);
        return query.getSingleResult();
    }

    private boolean isMarkNotValidValue(Integer mark){
        if(Objects.isNull(mark) || mark < 0) return true;
        return false;
    }
}
