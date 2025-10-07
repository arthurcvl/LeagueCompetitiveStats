package com.compstats.data_writer.model;

import jakarta.persistence.Entity;
import jakarta.persistence.Id;

@Entity()
public class Team {

    @Id
    private String teamId;

    private String teamName;

    private String teamLeague;

    public String getTeamId() {
        return teamId;
    }

    public void setTeamId(String teamId) {
        this.teamId = teamId;
    }

    public String getTeamName() {
        return teamName;
    }

    public void setTeamName(String teamName) {
        this.teamName = teamName;
    }

    public String getTeamLeague() {
        return teamLeague;
    }

    public void setTeamLeague(String teamLeague) {
        this.teamLeague = teamLeague;
    }

    public Team(String teamId, String teamName, String teamLeague) {
        this.teamId = teamId;
        this.teamName = teamName;
        this.teamLeague = teamLeague;
    }
}

/* <dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>

 */
