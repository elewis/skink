# Skink

Skink is a command-line tool that leverages OpenAI's chat API to help you build, modify, debug, and generate unit tests for your code. It can also generate a README file for your project based on the existing files in your project directory.

## Installation

To install Skink, you can use pip:

```
pip install -e .
```

This will install the required dependencies and make the `skink` command available in your terminal.

## Configuration

Before using Skink, you need to configure it with your OpenAI API key. You can do this by running:

```
skink configure
```

This will prompt you to enter your API key, which will be saved for future use.

## Usage

Skink provides several commands to help you with your code:

### Build

To build a new file with optional context files, use the `build` command:

```
skink build <file> [--context-files <file1> <file2> ...] [--model <model>]
```

The target file should already exist and should contain a description of the file that you are trying to build. The more specific the specification, the more accurate the result. As an example:

```
A python script with a function that does the following:
- accepts a URL string as a parameter
- raises an error if the URL is invalid
- scrapes the specified page for heading tags
- returns an array of resulting headings
```

The `--context-files` (or `-c`) option can be used to pass in one or more additional files that could provide useful reference. For example, you can pass in files containing modules that should be imported and used by the new file that is being built.

### Modify

To modify an existing file, use the `modify` command:

```
skink modify <file> [--request <request>] [--context-files <file1> <file2> ...] [--model <model>]
```

The request should be in the form of a command, such as "Add a new function that..." or "Refactor the existing class to...".

### Debug

To debug an existing file, use the `debug` command:

```
skink debug <file> [--error <error_message>] [--model <model>]
```

If an error message is not passed, this command will simply look for any possible issues in the given file.

### Generate Unit Tests

To generate a unit test file for an existing file, use the `spec` command:

```
skink spec <file> <target_path> [--model <model>]
```

Once they have been generated, test files can be further adjusted with the `modify` command.

### Generate README

To generate a README file for your project, use the `readme` command:

```
skink readme [--model <model>]
```

This command will gather all application files into context automatically. It will exclude a number of files irrelevant to a README, such as tests and licences. Please note, this currently only works for relatively small projects given the limited context window available for GPT.

## Models

Skink currently supports the following models:

- gpt-3.5-turbo (default)
- gpt-4

You can specify the model to use with the `--model` option for each command.

## Dependencies

Skink requires the following dependencies:

- click==8.1.3
- openai==0.27.2
- pytest==7.2.2
- setuptools==58.0.4

## Tests

Run the test suite using `pytest`.

## License

This project is licensed under the MIT License.
