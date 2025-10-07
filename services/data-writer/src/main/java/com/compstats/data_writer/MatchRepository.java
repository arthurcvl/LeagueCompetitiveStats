package com.compstats.data_writer;

import com.compstats.data_writer.model.Match;
import com.compstats.data_writer.model.MatchPK;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MatchRepository extends JpaRepository<Match, MatchPK> {
}
