package com.compstats.data_writer.model;

import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Data;

@Entity()
@IdClass(MatchPK.class)
public class Match {

    @Id
    private String matchId;

    @Id
    private String teamId;

    private String matchLeague;

    private String split;

    //This is something i will have to change in the future
    private String date;

    private Integer matchDuration;

    private int result;

    private Integer kills;

    private Integer dragons;

    private Integer towers;

    public Match() {
    }

    public String getMatchId() {
        return matchId;
    }

    public void setMatchId(String matchId) {
        this.matchId = matchId;
    }

    public String getTeamId() {
        return teamId;
    }

    public void setTeamId(String teamId) {
        this.teamId = teamId;
    }

    public String getMatchLeague() {
        return matchLeague;
    }

    public void setMatchLeague(String matchLeague) {
        this.matchLeague = matchLeague;
    }

    public String getSplit() {
        return split;
    }

    public void setSplit(String split) {
        this.split = split;
    }

    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public Integer getMatchDuration() {
        return matchDuration;
    }

    public void setMatchDuration(Integer matchDuration) {
        this.matchDuration = matchDuration;
    }

    public int getResult() {
        return result;
    }

    public void setResult(int result) {
        this.result = result;
    }

    public Integer getKills() {
        return kills;
    }

    public void setKills(Integer kills) {
        this.kills = kills;
    }

    public Integer getDragons() {
        return dragons;
    }

    public void setDragons(Integer dragons) {
        this.dragons = dragons;
    }

    public Integer getTowers() {
        return towers;
    }

    public void setTowers(Integer towers) {
        this.towers = towers;
    }

    @Override
    public String toString() {
        return "Match{" +
                "matchId='" + matchId + '\'' +
                ", teamId='" + teamId + '\'' +
                ", matchLeague='" + matchLeague + '\'' +
                ", split='" + split + '\'' +
                ", date='" + date + '\'' +
                ", matchDuration=" + matchDuration +
                ", result=" + result +
                ", kills=" + kills +
                ", dragons=" + dragons +
                ", towers=" + towers +
                '}';
    }
}
