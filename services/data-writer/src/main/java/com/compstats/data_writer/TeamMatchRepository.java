package com.compstats.data_writer;

import com.compstats.data_writer.model.MatchPK;
import com.compstats.data_writer.model.TeamMatch;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TeamMatchRepository extends JpaRepository<TeamMatch, MatchPK> {
}
