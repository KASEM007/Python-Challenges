# Oscar Winners
# Provide a list with the name(s) of the director(s) with the most Oscar wins.
# We are asking for a list because there could be more than 1 director tied
# for the most Oscar wins.

winners = {
    1931: ["Norman Taurog"],
    1932: ["Frank Borzage"],
    1933: ["Frank Lloyd"],
    1934: ["Frank Capra"],
    1935: ["John Ford"],
    1936: ["Frank Capra"],
    1937: ["Leo McCarey"],
    1938: ["Frank Capra"],
    1939: ["Victor Fleming"],
    1940: ["John Ford"],
    1941: ["John Ford"],
    1942: ["William Wyler"],
    1943: ["Michael Curtiz"],
    1944: ["Leo McCarey"],
    1945: ["Billy Wilder"],
    1946: ["William Wyler"],
    1947: ["Elia Kazan"],
    1948: ["John Huston"],
    1949: ["Joseph L. Mankiewicz"],
    1950: ["Joseph L. Mankiewicz"],
    1951: ["George Stevens"],
    1952: ["John Ford"],
    1953: ["Fred Zinnemann"],
    1954: ["Elia Kazan"],
    1955: ["Delbert Mann"],
    1956: ["George Stevens"],
    1957: ["David Lean"],
    1958: ["Vincente Minnelli"],
    1959: ["William Wyler"],
    1960: ["Billy Wilder"],
    1961: ["Jerome Robbins", "Robert Wise"],
    1962: ["David Lean"],
    1963: ["Tony Richardson"],
    1964: ["George Cukor"],
    1965: ["Robert Wise"],
    1966: ["Fred Zinnemann"],
    1967: ["Mike Nichols"],
    1968: ["Carol Reed"],
    1969: ["John Schlesinger"],
    1970: ["Franklin J. Schaffner"],
    1971: ["William Friedkin"],
    1972: ["Bob Fosse"],
    1973: ["George Roy Hill"],
    1974: ["Francis Ford Coppola"],
    1975: ["Milos Forman"],
    1976: ["John G. Avildsen"],
    1977: ["Woody Allen"],
    1978: ["Michael Cimino"],
    1979: ["Robert Benton"],
    1980: ["Robert Redford"],
    1981: ["Warren Beatty"],
    1982: ["Richard Attenborough"],
    1983: ["James L. Brooks"],
    1984: ["Milos Forman"],
    1985: ["Sydney Pollack"],
    1986: ["Oliver Stone"],
    1987: ["Bernardo Bertolucci"],
    1988: ["Barry Levinson"],
    1989: ["Oliver Stone"],
    1990: ["Kevin Costner"],
    1991: ["Jonathan Demme"],
    1992: ["Clint Eastwood"],
    1993: ["Steven Spielberg"],
    1994: ["Robert Zemeckis"],
    1995: ["Mel Gibson"],
    1996: ["Anthony Minghella"],
    1997: ["James Cameron"],
    1998: ["Steven Spielberg"],
    1999: ["Sam Mendes"],
    2000: ["Steven Soderbergh"],
    2001: ["Ron Howard"],
    2002: ["Roman Polanski"],
    2003: ["Peter Jackson"],
    2004: ["Clint Eastwood"],
    2005: ["Ang Lee"],
    2006: ["Martin Scorsese"],
    2007: ["Ethan Coen", "Joel Coen"],
    2008: ["Danny Boyle"],
    2009: ["Kathryn Bigelow"],
    2010: ["Tom Hooper"],
}

# Here's the logic for my solution:
# To address this question, I will need to first create a dictionary
# with the number of wins by each winning director.

# First Part of the Solution:

win_count_dict = {}
for year, winner_list in winners.items():
    for winner in winner_list:
        win_count_dict[winner] = win_count_dict.get(winner, 0) + 1


# Second Part of Solution:

# This win_count_dict dictionary provides a dictionary with the win count for
# the directors.
# We will need this to then identify which key (here, director name) has the
# highest value (here, win count).
# To perform this task, we use a variable highest_count to keep track of the
# highest count of wins.
# We iterate through the dictionary to see
# if the value for a key (i.e., wins for a director) is more than the highest count.
# If it is, we replace that value as the highest_count.
# Plus we add that key (here, director name) to our list tracking the most_win_director.
# Every time we come upon a value higher than the current highest_count,
# we replace highest_count with the new higher value, empty the most_win_director
# and replace it with the new key (i.e., director's name).

# highest_count = 0
# most_win_director = []

# for key, value in win_count_dict.items():
#     if value > highest_count:
#         highest_count = value
#         most_win_director.clear()
#         most_win_director.append(key)
#     elif value == highest_count:
#         most_win_director.append(key)
#     else:
#         continue


# print(f"most_win_director = {most_win_director}")


################################## Better Solution ###########################

# Here is an alternative compact solution to replace the 12 lines above
# for the second part of the solution, using the built-in function max(),
# and a list comprehension with a condition:


highest_count = max(win_count_dict.values())

most_win_director = [
    key for key, value in win_count_dict.items() if value == highest_count
]

print(f"most_win_director = {most_win_director}")
