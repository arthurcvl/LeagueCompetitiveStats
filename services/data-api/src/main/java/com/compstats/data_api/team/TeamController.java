package com.compstats.data_api.team;

import com.compstats.data_api.team.model.Team;
import org.apache.coyote.BadRequestException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("api")
public class TeamController {

    @Autowired
    private TeamService teamService;

    @GetMapping("/teams/headers")
    public ResponseEntity<List<Team>> getAllTeamsData(){
        return ResponseEntity.ok(teamService.getALl());
    }

    @GetMapping("/team/{name}")
    public ResponseEntity<Team> get(@PathVariable String name) throws BadRequestException {
        return ResponseEntity.ok(teamService.getByName(name));
    }


}
