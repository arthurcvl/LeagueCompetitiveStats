package com.compstats.data_api.match.model;

import com.compstats.data_api.team.model.Team;
import com.fasterxml.jackson.annotation.JsonBackReference;
import com.fasterxml.jackson.annotation.JsonManagedReference;
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
    
    @ManyToOne
    @JoinColumn(name = "matchId", insertable = false, updatable = false)
    @JsonBackReference
    private Match match;
    
    @ManyToOne
    @JoinColumn(name = "teamId", insertable = false, updatable = false)
    @JsonBackReference
    private Team team;
    
    private Integer teamKills;
    
    private Integer teamDragons;

    private Integer teamTowers;

    private int result;

    //This should be a enum for data safety reasons?
    //TODO
    private String teamSide;

}
