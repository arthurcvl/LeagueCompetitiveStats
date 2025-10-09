package com.compstats.data_api.team;

import com.compstats.data_api.team.model.Team;
import com.compstats.data_api.team.persistence.TeamRepository;
import org.apache.coyote.BadRequestException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TeamService {

    @Autowired
    private TeamRepository teamRepository;

    public List<Team> getALl() {
        return teamRepository.findAll();
    }


    public Team getByName(String name) throws BadRequestException {
        return teamRepository.findByTeamName(name)
                .orElseThrow(() -> new BadRequestException("Team not found!"));
    }

    /*private Integer calculateAvaregeByTeamStatusName(){
        return teamRepository.getAverageByTeamNameStatus();
    }*/
}
