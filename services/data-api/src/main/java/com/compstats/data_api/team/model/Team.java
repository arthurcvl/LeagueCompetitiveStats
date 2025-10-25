package com.compstats.data_writer.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;
import jakarta.persistence.OneToMany;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.util.List;

@Entity
@Data
@NoArgsConstructor
public class Team {

    @Id
    private String teamId;

    private String teamName;

    private String teamLeague;

    @OneToMany(mappedBy = "team")
    private List<TeamMatch> teamMatch;
}