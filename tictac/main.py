from tictac.board import play_games
from tictac.board import play_random_move
from tictac.mcts import play_mcts_move, perform_training_playouts

print("Playing random vs random:")
print("-------------------------")
play_games(1000, play_random_move, play_random_move)
print("")

print("Training MCTS...")
perform_training_playouts()
print("")
print("Playing random vs MCTS:")
print("-----------------------")
play_games(1000, play_random_move, play_mcts_move)
print("")
print("Playing MCTS vs random:")
print("-----------------------")
play_games(1000, play_mcts_move, play_random_move)
print("")
print("Playing MCTS vs MCTS:")
print("---------------------")
play_games(1000, play_mcts_move, play_mcts_move)
print("")
