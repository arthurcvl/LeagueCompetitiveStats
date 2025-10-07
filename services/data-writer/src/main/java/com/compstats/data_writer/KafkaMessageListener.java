package com.compstats.data_writer;

import com.compstats.data_writer.model.Match;
import com.compstats.data_writer.model.Team;
import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.kafka.annotation.KafkaListeners;
import org.springframework.stereotype.Component;

@Component
public class KafkaMessageListener {

    @Autowired
    ObjectMapper objectMapper;

    @Autowired
    MatchRepository matchRepository;

    @Autowired
    TeamRepository teamRepository;

    @KafkaListener(
            topics = "data_producer.teams.team_created.json",
            groupId = "test"
    )
    void listenTeams(String message) throws JsonProcessingException {
        Team team = objectMapper.readValue(message, Team.class);
        teamRepository.save(team);
    }

    @KafkaListener(
            topics = "data_producer.matches.match_finished.json",
            groupId = "test1"
    )
    void listenMatches(String message) throws JsonProcessingException {
        Match match = objectMapper.readValue(message, Match.class);
        matchRepository.save(match);
    }
}
