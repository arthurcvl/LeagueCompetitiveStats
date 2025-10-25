package com.compstats.data_writer.model;

import jakarta.persistence.*;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity()
@IdClass(MatchPK.class)
@NoArgsConstructor
@Data
public class TeamMatch {

    @Id
    private String matchId;

    @Id
    private String teamId;

    private Integer kills;

    private Integer dragons;

    private Integer towers;

    private int result;

}
