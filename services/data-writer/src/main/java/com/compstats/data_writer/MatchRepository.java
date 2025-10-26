package com.compstats.data_writer;

import com.compstats.data_writer.model.Match;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MatchRepository extends JpaRepository<Match, String> {
}
