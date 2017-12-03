## Installing the Delegate

First, replace the IssuesMonitoring default `db` folder with the delegate's `./db/`:
`rm -r ~/IssuesMonitoring/server/db/`
`cp ./DelegateFiles/db/ ~/IssuesMonitoring/server/`

Then add the Delegate's controller, model and view:
`cp ./DelegateFiles/controller/delegate.py ~/IssuesMonitoring/server/controllers`
`cp ./DelegateFiles/model/delegate.py ~/IssuesMonitoring/server/views`
`cp ./DelegateFiles/view/delegate.py ~/IssuesMonitoring/server/models`

Now you can proceed with the normal installation process for IssuesMonitoring.

A functionality test file is provided at `DelegateFiles/test_endpoints` for simulating IssuesAppthenticator requests and a fully working demo of IssuesMonitoring with the Delegate is provided at `./IssuesMonitoringWithDelegate`. 
