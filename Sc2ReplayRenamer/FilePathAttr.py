from abc import ABC, abstractmethod

class FilePathAttr(ABC):
    
    def __init__(self, replay_file):
        super().__init__()
        
        self._filepath_attributes = {
                'game-type' : '',
                'matchup' : '',
                'format' : '',
                'date' : '',
                'teams' : '',
                'map' : '',
                'length' : ''
            }

        self._replay = self._load_replay(replay_file)
        self._process_filepath_attributes(self._replay)


    def getAttributes(self):
        return self._filepath_attributes

    @abstractmethod
    def _load_replay(self, replay_file):
        pass

    @abstractmethod
    def _get_game_type(self, replay):
        pass

    @abstractmethod
    def _get_matchup(self, replay):
        pass

    @abstractmethod
    def _get_game_format(self, replay):
        pass

    @abstractmethod
    def _get_date(self, replay, datestring="%Y-%m-%D"):
        pass

    @abstractmethod
    def _get_teams(self, replay, teamstring="{name}"):
        pass

    @abstractmethod
    def _get_map(self, replay):
        pass

    @abstractmethod
    def _get_length(self, replay):
        pass

    def _process_filepath_attributes(self, replay):
        filepath_attributes['game-type'] = get_game_type(replay)
