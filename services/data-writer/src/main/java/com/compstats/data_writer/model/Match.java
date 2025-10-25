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
public class Match {

    @Id
    private String matchId;

    private String matchLeague;

    private String split;

    private String date;

    private Integer matchDuration;

    @OneToMany(mappedBy = "match")
    private List<TeamMatch> teamMatch;
}
