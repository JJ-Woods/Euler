#Author - Jamie Woods
#https://projecteuler.net/problem=13

#This solution involves the summation of 100 50 digit numbers, to save copying them out needlessly I get them
#from the problem website and store them in a scratch file

from pathlib import Path
import urllib.request
import time

PROBLEM_LINK = "https://projecteuler.net/problem=13"
SCRATCH_FILE = "/Scratch/pe013.txt"
SIG_FIGS = 10


def main():
    start = time.time()
    if check_scratch_exists():
        data_grid = get_data_from_scratch()
    else:
        data_grid = get_data_from_html()
    solution = find_sum_of_grid(data_grid, SIG_FIGS)
    end = time.time()
    time_taken = end - start
    print("The solution to problem 13 is " + str(solution) + "; Time taken is " + str(time_taken) + " seconds.")


def check_scratch_exists():
    my_file = Path("/path/to/file")
    if my_file.is_file():
        return True
    else:
        return False


def get_data_from_scratch():
    return True


def get_data_from_html():
    return True


#Get all html for a given link
def get_html(link):
    page = urllib.request.urlopen(link)
    page_bytes = page.read()
    html = page_bytes.decode("utf8")
    page.close()
    return html


def find_sum_of_grid(data_grid, sig_figs):
    return 0


if __name__ == "__main__":
    main()
