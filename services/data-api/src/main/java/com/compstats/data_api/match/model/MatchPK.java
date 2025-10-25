package com.compstats.data_api.match.model;

import java.io.Serializable;
import java.util.Objects;

@Getter
@NoArgsConstructor
public class MatchPK implements Serializable {
    private String matchId;
    private String teamId;

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
