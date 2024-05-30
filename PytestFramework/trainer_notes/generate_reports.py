To generate the reports, first we have to install the plugin

* Go to command proompt --> pip install pytest-html

* To generate the reports -->   right click--> open in--> terminal -->
                                pytest test_filename.py -vs --html="report_name.html"

    The report will be stored in the same folder as the test file

* To generate the reports in different folder -->
        pytest test_filename.py -vs --html="folder_path/report_name.html"