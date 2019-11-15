# algolearn - a 16-bit "learner computer" in Python 

algolearn provides a very simple "learner computer" in Python to solve foundational algorithmic challenges
that has historically been taught in Pascal, C or even Basic.

You write programs in Python and have access to a "VM" with 16 bit memory (64k in 64 byte pages).
There are only limited instructions available and you need to learn about pointers. 

Running
=======

Currently it's all quite simple, you can simply use Python 3.5 from your system without dependencies. 

```
$ python3 l1.py <yourprogram>
```

There are a number of boilerplates that you can use to get started:

```
$ python3 l1.py linkedlist.py
```

API
===

Here's the available instructions:

* **malloc**(size) -> address
* **free**(address)
* **write**(address, value)
* **read**(address) -> value
* **write_addr**(address, value_address)
* **read_addr**(address)
  
And the data types:

* values - are single bytes (8-bit, 0..255)
* addresses - are words (16-bit, 0..2^16-1)

Additionally you can access a constant:

* PAGESIZE (could vary, default is 64 bytes) 

Notes
=====

* The zero page is pre-allocated and used for system purposes (really, real machines would have
  those for ROMs but I just want to not use it to avoid null pointer confusion and I don't want to necessarily
  have virtual memory (yet))
  
* The VM performs a certain amount of accounting and assigns a cost to every operation and reports on it at the end.
  The specific cost is assigned in a "strategic" way for teaching, not for ultra realistic simulation.

* I'm pondering to add RestrictedPython to the mix so that specific VMs can limit what the students have access to.
  However, I do want them to be able to take some convenience shortcuts (accessing print and output formatting)
  so they can focus on the algorithm. I likely want to reduce access to higher order data types (lists, sets) etc
  so that I don't have to manually review the code for unintended overreach.

Future
======

We're using this for our apprentices and if this takes off then I might create multiple VM implementations iwth


