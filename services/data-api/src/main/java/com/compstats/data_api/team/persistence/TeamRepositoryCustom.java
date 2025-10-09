package com.compstats.data_api.team.persistence;

import com.compstats.data_api.team.enums.ComparisonType;

public interface TeamRepositoryCustom {

    Double getAverageByTeamNameStatus(String teamName, String statusName);
    Double getRelativeFrequencyByTeamNameStatus(String teamName, String statusName, Integer mark, ComparisonType comparisonType);

}
