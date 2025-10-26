package com.compstats.data_api.team.model;

import com.compstats.data_api.match.model.TeamMatch;
import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonManagedReference;
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
    @JsonManagedReference
    private List<TeamMatch> teamMatches;
}