package com.compstats.data_api.team.model;

import com.compstats.data_api.match.model.Match;
import com.fasterxml.jackson.annotation.JsonManagedReference;
import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;

import java.util.ArrayList;
import java.util.List;

@Entity()
public class Team {

    @Id
    private String teamId;

    private String teamName;

    private String teamLeague;

    //vou dar uma explicada sobre essa notação para eu relembrar depois:
    /* o @OneToMany (pelo menos nao nesse caso) nao interferi no lado do banco de dados
    e esse "mapeamento" da lista de partidas é feito somente no lado do spring, por isso que o mappedBy
    é o nome do atributo no lado do Many e nao o nome da FK do Many, pois esse mapeamento somente acontece
    no lado do spring
     */

    @OneToMany(mappedBy = "team")
    @JsonManagedReference
    private List<Match> matches = new ArrayList<>();

    public List<Match> getMatches() {
        return matches;
    }

    public String getTeamId() {
        return teamId;
    }

    public void setTeamId(String teamId) {
        this.teamId = teamId;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public String getTeamLeague() {
        return teamLeague;
    }

    public void setTeamLeague(String teamLeague) {
        this.teamLeague = teamLeague;
    }

    public Team() {
    }
}

