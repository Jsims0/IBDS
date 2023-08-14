# Reading and writing files in Python

* First print out (or view) reference card:
  *  [fileio_in_python.pdf](
     ../.instructions/1_file_io/fileio_in_python.pdf)
     (PDF for printing)
  *  [fileio_in_python.md](
     ../.instructions/1_file_io/fileio_in_python.md)
     (markdown for viewing)

* Then work through the mini-exercises below to introduce Python fileIO.
* All of the starting Python files can be found in the `1_file_io/` subdirectory
  of the assignment repo. So open a terminal cd into the assignment repo and then
  ```
  cd 1_file_io
  ```
* For each mini-exercise it is best to try the exercise yourself, 
  and compare my approach to your solution, looking at the video and/or
  git commits given. If get stuck use the video as a follow me exercise
  doing exactly what is shown. After each video you can find GitHub links to
  the commits made that give full details as to the code changes.

#### Mini-exercise 1a. Read a text file and print out its contents.
* Python file (with instructions) [mini_1a_read_a_file.py](./mini_1a_read_a_file.py)
* [![Start MyPlayer "Read a text file and print out its contents"](
      ../.instructions/1_file_io/h1a_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9850 
      "Start MyPlayer Read a text file and print out its contents")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9850)
* GitHub links to the commits made in video:
  * [reads example_in.txt successfully.](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/54d1fff984cedf3ff7545136cf55706be9c4daec)
  * [Alternative open file using with.](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/344a364a3ab125929ca6de23df9141391b137f63)


#### Mini-exercise 1b. Write function to read a file and return list of lines
* Python file (with instructions) [mini_1b_function_to_read_a_file_into_lines.py](
                                 ./mini_1b_function_to_read_a_file_into_lines.py)
* [![Start MyPlayer "Write function to read a file and return list of lines"](
      ../.instructions/1_file_io/h1b_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9853 
      "Start MyPlayer Write function to read a file and return list of lines")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9853)
* GitHub link to the commit made in video 
  * [lines_from_file() now works. passes test_lines_from_file:](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/dc821aa78499b29a246ebf3f39b5c8c91e497389)
 

#### Mini-exercise 1c. Write a FASTA sequence file 
* Python file (with instructions) [mini_1c_write_a_file.py](./mini_1c_write_a_file.py)
* [![Start MyPlayer "Write a FASTA sequence file"](
      ../.instructions/1_file_io/h1c_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9854 
      "Start MyPlayer: Write a FASTA sequence file")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9854)
* GitHub links to the commits made in video:
  * [Write the FASTA. Manual Test:](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/0c28a738c5fda67ff31fb2a51e0f1eb7066185cb)
  * [change to 'with open() as ...'.](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/b5ee1d09caaa8dec55ce534c92832c1d8833e196)

#### Mini-exercise 1d. Read a CSV file
* Python file (with instructions) [mini_1d_read_a_csv_file.py](./mini_1d_read_a_csv_file.py)
* [![Start MyPlayer "Read a CSV file"](
      ../.instructions/1_file_io/h1d_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9856 
      "Start MyPlayer: Read a CSV file")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9856)
* GitHub links to the commits made in video:
  * [read the CSV file and prints out information:](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/1f0abcc3ef2d9830b2ba7ef7e9f3cdaaa2e0d659)
  * [Make output more readable by separating fields with spaces.](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/a1b948ace5f44b5f5fb8ed5c09e9d4903fff6182)


#### Mini-exercise 1e. Read a TSV file, modify things and write out as CSV file
* Python file (with instructions) [mini_1e_read_tsv_write_csv.py](./mini_1e_read_tsv_write_csv.py)
* [![Start MyPlayer "Read a TSV file, modify things and write out as CSV file"](
      ../.instructions/1_file_io/h1e_myplayer_screenshot.png?raw=true)](
      https://myplayer.anglia.ac.uk/Player/9858 
      "Start MyPlayer: Read a TSV file, modify things and write out as CSV file")
      [*MyPlayer link*](https://myplayer.anglia.ac.uk/Play/9858)
* GitHub links to the commits made in video:
  * [Reads the input TSV, does the required replace & with and and](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/a57a894eea43af10a4cafebeafa6b5c21f45f91d)
  * [Write the output lmb_out.csv file as per instructions](https://github.com/ARU-Bioinf-IBDS/assignment-H-osmart/commit/078743f32cb2f9f52355be121a80adb6e63c8ee1)



<hr>

*Back to:* [Instructions for Assignment H: Unit tests and File IO](../.instructions/README.md)
