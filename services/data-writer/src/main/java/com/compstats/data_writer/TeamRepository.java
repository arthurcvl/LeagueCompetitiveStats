package com.compstats.data_writer;

import com.compstats.data_writer.model.Team;
import org.springframework.data.jpa.repository.JpaRepository;

public interface TeamRepository extends JpaRepository<Team, String> {
}
