import unittest
from unittest.mock import mock_open, patch
from assignment.task_1.ReleasePlanner import main


class TestReleasePlanner(unittest.TestCase):

    def setUp(self):
        self.input_data = (
            "1 1\n"
            "2 1\n"
            "3 1\n"
            "9 1\n"
            "10 4\n"
            "10 2\n"
            "9 5\n"
            "10 3\n"
            "4 5\n"
        )

        self.output_data = (
            "5\n"
            "1 1\n"
            "2 2\n"
            "3 3\n"
            "4 8\n"
            "9 9\n"
        )

        self.non_integer_input_data = "1 1\n2 x\n3 1\n"
        self.incorrect_format_input_data = "1 1\n2\n3 1\n"

    @patch('builtins.open')
    def test_selecting_max_releases(self, mock_open_file):
        mock_input_file = mock_open(read_data=self.input_data).return_value
        mock_output_file = mock_open().return_value
        mock_open_file.side_effect = [mock_input_file, mock_output_file]

        main()

        write_calls = mock_output_file.write.call_args_list
        selected_releases = [args[0] for args, _ in write_calls]

        output_list = self.output_data.strip().split('\n')
        expected_releases = [line + '\n' for line in output_list]

        self.assertEqual(selected_releases, expected_releases)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_input_file_not_found(self, mock_open_file):
        with self.assertRaises(FileNotFoundError):
            main()

    @patch('builtins.open')
    def test_non_integer_values(self, mock_open_file):
        mock_input_file = mock_open(read_data=self.non_integer_input_data).return_value
        mock_open_file.side_effect = [mock_input_file]
        with self.assertRaises(ValueError) as error:
            main()
        self.assertIn("Non-integer value found", str(error.exception))

    @patch('builtins.open')
    def test_incorrect_format(self, mock_open_file):
        mock_input_file = mock_open(read_data=self.incorrect_format_input_data).return_value
        mock_open_file.side_effect = [mock_input_file]
        with self.assertRaises(ValueError) as error:
            main()
        self.assertIn("Invalid format", str(error.exception))


if __name__ == '__main__':
    unittest.main()
