# OpenHaystake Toolkit


# Keygen

```shell
./keygen.py
```

Generates a new airtag keys
```json
{
    "key_id": "DIf2Od7NcEfYHsFVQTC/xTUFecr3J8B0KoPfJHsXRQM=",
    "advertisement_key": "f9dQjCafB68gi9ZKLH/iQsN9tScDX+zXF4BfZGDqoyA=",
    "private_key": "7b1MPYzazUCpDzTUDO9RM2h+2VytFGe0Sdua8A=="
}
```

# Flashing

```shell
 ./flash.py --advertisement-key=$KEY

Open On-Chip Debugger 0.12.0
Licensed under GNU GPL v2
For bug reports, read
	http://openocd.org/doc/doxygen/bugs.html
WARNING: interface/stlink-v2.cfg is deprecated, please switch to interface/stlink.cfg
Info : auto-selecting first available session transport "hla_swd". To override use 'transport select <transport>'.
Info : The selected transport took over low-level target control. The results might differ compared to plain JTAG/SWD
Info : clock speed 1000 kHz
Info : STLINK V2J25S4 (API v2) VID:PID 0483:3748
Info : Target voltage: 3.234442
Info : [nrf51.cpu] Cortex-M0 r0p0 processor detected
Info : [nrf51.cpu] target has 4 breakpoints, 2 watchpoints
Info : starting gdb server for nrf51.cpu on 3333
Info : Listening on port 3333 for gdb connections
[nrf51.cpu] halted due to debug-request, current mode: Handler HardFault
xPSR: 0x41000003 pc: 0x00000c7a msp: 0x20003fd0
Info : nRF51822-QFAA(build code: H0) 256kB Flash, 16kB RAM
Info : Mass erase completed.
Info : A reset or power cycle is required if the flash was protected before.
[nrf51.cpu] halted due to debug-request, current mode: Thread
xPSR: 0xc1000000 pc: 0xfffffffe msp: 0xfffffffc
** Programming Started **
Warn : Adding extra erase range, 0x0000374c .. 0x000037ff
** Programming Finished **
** Verify Started **
** Verified OK **
[nrf51.cpu] halted due to debug-request, current mode: Thread
xPSR: 0xc1000000 pc: 0x00000c3c msp: 0x20004000
** Programming Started **
Warn : Adding extra erase range, 0x0000374c .. 0x000037ff
** Programming Finished **
Info : Listening on port 6666 for tcl connections
Info : Listening on port 4444 for telnet connections
```

## Get locations
```shell
ICLOUD_KEY=<> ./locations.py tracker.json
```

trackers.json example

```json
[
	{
		"name": "My tracker",
		"key_id": "DIf2Od7NcEfYHsFVQTC/xTUFecr3J8B0KoPfJHsXRQM=",
		"advertisement_key": "f9dQjCafB68gi9ZKLH/iQsN9tScDX+zXF4BfZGDqoyA=",
		"private_key": "7b1MPYzazUCpDzTUDO9RM2h+2VytFGe0Sdua8A=="
	}
]
```