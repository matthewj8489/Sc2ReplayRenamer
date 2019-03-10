import FilePathAttr

class Sc2ReaderFilePathAttr(FilePathAttr):

    def __init__(self, replay_file):
        super().__init__(replay_file)

    def _load_replay(self, replay_file):
        return sc2reader.load_replay(replay_file)

    def _get_game_type(self, replay):
        pass

    def _get_matchup(self, replay):
        pass

    def _get_game_format(self, replay):
        pass

    def _get_date(self, replay, datestring="%Y-%m-%D"):
        pass

    def _get_teams(self, replay, teamstring="{name}"):
        pass

    def _get_map(self, replay):
        pass

    def _get_length(self, replay):
        pass

