# Gitlab Pipeline Monitor

Python script that will blink a LED when the pipeline fails using a Raspberry Pi. 


### Prerequisites

What things you will need to build the monitor

- Raspberry Pi
- Small LED
- Wires


## Getting Started

* Clone this repository and enter the folder
```bash
git clone https://github.com/hewerthomn/pipeline-monitor.git
cd pipeline-monitor
```
* Create a env file and setup the environment constants.
```bash
cp .env.example .env
```
* Run the script `pipelines.py`
```bash
python3 pipelines.py
```

## Built With

* Python 3
* Gitlab API V4


## Authors

* **Éverton Inocêncio** - *Initial work* - [hewerthomn](https://github.com/hewerthomn)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
