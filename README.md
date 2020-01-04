# Airtable Markdown Calendar

## About
Takes an Airtable calendar csv and turns it into a markdown calendar (Compatible with GFM).
<table>
  <tbody align="left">
  <tr>
      <th>Post Title</th>
      <th>Status</th>
      <th>Publish Date / Time</th>
      <th>Issue</th>
      <th>Author</th>
    </tr>
    <tr>
      <td>Post 1</td>
      <td>Stat 1</td>
      <td>Date 1</td>
      <td><a href="https://github.com/blog/issues/1">#1</a></td>
      <td>Author 1</td>
    </tr>
    <tr>
      <td>Post 2</td>
      <td>Stat 2</td>
      <td>Date 2</td>Â
      <td><a href="https://github.com/blog/issues/2">#2</a></td>
      <td>Author 2</td>
    </tr>
  </tbody>
</table><br  />

This calendar...
- Trims any leading/trailing whitespace from each table cell
- Replaces links to GitHub issues with shorter text (e.g. #42)
- Aligns all table data to the left

## Getting started

### Prerequisites
- Python3
    ```sh
    brew install python3
    ```

### Installation & Usage
1. Clone the repo
    ```sh
    git clone https://github.com/dansjack/airtable-markdown-calendar.git
    ```
2. start the program
    ```sh
    python3 airtable-markdown-calendar
    ```
3. Follow the prompt to generate a calendar. The calendar will appear under the airtable-markdown-calendar
directory

&nbsp; &nbsp; &nbsp; &nbsp; _Example_: Answer the prompts as they're shown below to print an example calendar<br>
```sh
*****************************************
***** AIRTABLE TO MARKDOWN CALENDAR *****
*****************************************

Enter the relative path of an Airtable csv file: src/test/test_infile
Enter the name of your new calendar: my_new_calendar

*****************************
********** GOODBYE **********
*****************************

```
&nbsp; &nbsp; &nbsp; &nbsp; New calendar now at `airtable-markdown-calendar/my_new_calendar`
