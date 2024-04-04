import pandas as pd

states = ["California", "Texas", "Florida", "New York"]
population = [39613493, 29730311, 21944577, 19299981]

dict_states = {'States': states, 'Population': population}

df_states = pd.DataFrame.from_dict(dict_states)
# print(df_states)
# index=False gets rid of the index. 0, 1, 2, so on
df_states.to_csv('states.csv', index=False)

# print(states[-4])

# for state in states:
#     if state == "Florida":
#         print(state)

# open('filename', 'modes') takes in a file name and mode
# w creates the file in current directory, deletes if it exist, etc
# with will close the file as soon as its done
# as replaces open.... to file
# with open('test.txt', 'w') as file:
#     file.write("Data succesfully scraped!")