from tqdm import tqdm
import time

def create_cli_progress_bar_animation(total_steps: int, sleep_time: float = 0.1, desc: str = "Progress") -> None:
    """
    Creates a CLI progress bar animation.

    Args:
    total_steps (int): The total number of steps in the progress bar.
    sleep_time (float): The time to sleep between each step. Defaults to 0.1.
    desc (str): The description of the progress bar. Defaults to "Progress".
    """
    for _ in tqdm(range(total_steps), desc=desc):
        # Simulate some work being done
        time.sleep(sleep_time)

# Example usage
if __name__ == "__main__":
    total_steps = 100
    create_cli_progress_bar_animation(total_steps)