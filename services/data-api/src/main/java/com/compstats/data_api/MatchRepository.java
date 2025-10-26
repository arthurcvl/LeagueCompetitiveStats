package com.compstats.data_api;

import com.compstats.data_api.match.model.Match;
import org.springframework.data.jpa.repository.JpaRepository;

public interface MatchRepository extends JpaRepository<Match, String> {
}
