package com.compstats.data_writer.model;

import java.io.Serializable;
import java.util.Objects;

public class MatchPK implements Serializable {
    private String matchId;
    private String teamId;

    public String getMatchId() {
        return matchId;
    }

    public String getTeamId() {
        return teamId;
    }

    @Override
    public boolean equals(Object o) {
        if (o == null || getClass() != o.getClass()) return false;
        MatchPK matchPK = (MatchPK) o;
        return Objects.equals(matchId, matchPK.matchId) && Objects.equals(teamId, matchPK.teamId);
    }

    @Override
    public int hashCode() {
        return Objects.hash(matchId, teamId);
    }
}
