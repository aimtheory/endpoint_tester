# endpoint_tester
Python script to test a series of endpoints. It accepts a CSV input and create a CSV output with endpoint status and number of hops required to reach the endpoint in a traceroute operation.

Must be run as root for access to network interfaces.

## Usage
Takes input of a CSV file formatted like:
```commandline
domain.name,80,443,
otherdomain.name, 80, 443
```
Provides a CSV output in `./check_results.csv` of:
```commandline
domain.name,open, open, 11
otherdomain.name, open, closed, 13
```