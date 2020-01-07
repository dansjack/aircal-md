# aircal-md

## About
Aircal-md takes a csv file of an Airtable calendar as input, reads it, and outputs a markdown version of the calendar. (Compatible with Github Flavored Markdown).
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
      <td><a href="https://link.to.nowhere1">#1</a></td>
      <td>Author 1</td>
    </tr>
    <tr>
      <td>Post 2</td>
      <td>Stat 2</td>
      <td>Date 2</td>
      <td><a href="https://link.to.nowhere2">#2</a></td>
      <td>Author 2</td>
    </tr>
  </tbody>
</table><br  />
This calendar:  

- Trims any leading/trailing whitespace from each table cell
- Shortens link text (e.g. Link to a GitHub Issue would just state the number, like #42)
- Aligns all table data to the left

### Development plans
- [ ] Add option to choose result file location
- [ ] Add option to connect to the Airtable API to get a calendar instead of a csv file
- [ ] Add options to add/remove fields from the calendar

## Getting started

### Prerequisites
- Python3  


  There are different ways you can install Python. See [The Hitchhikers Guide to Python](https://docs.python-guide.org/starting/installation/) for detailed instructions. If you have Homebrew installed already, you can run the following to install Python3:
  
  ```sh
  $ brew install python
  ```

### Installation & Usage
1. Clone the repo
    ```sh
    $ git clone https://github.com/dansjack/aircal-md.git
    ```
2. start the program
    ```sh
    $ python3 aircal-md
    ```
3. Follow the prompt to generate a calendar. The calendar will appear under the aircal-md
directory

    _Example_: Answer the prompts as they're shown below to print an example calendar from the [Airtable content calendar template](https://airtable.com/templates/content-production/exp3FNmOkdHZvprXB/digital-content-calendar)<br>
      ```
      *****************************************
      *************   AIRCAL-MD   *************
      *****************************************

      Enter the relative path of an Airtable csv file: test_infile
      Enter the name of your new calendar: my_new_calendar

      *****************************
      ********** GOODBYE **********
      *****************************

      ```
  New calendar now at `aircal-md/results/my_new_calendar`
