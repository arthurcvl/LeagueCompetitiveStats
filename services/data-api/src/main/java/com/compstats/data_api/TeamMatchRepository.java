package com.compstats.data_api;

import com.compstats.data_api.match.model.MatchPK;
import com.compstats.data_api.match.model.TeamMatch;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TeamMatchRepository extends JpaRepository<TeamMatch, MatchPK> {
}
