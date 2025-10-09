package com.compstats.data_api.team.persistence;

import com.compstats.data_api.team.model.Team;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface TeamRepository extends JpaRepository<Team, String> {
    Optional<Team> findByName(String name);

}
