#!/usr/bin/env python3
import os
import socket

from src.c3tt_rpc_client import C3TTClient


def main():
    cli = C3TTClient(os.environ['CRS_TRACKER'], os.environ['CRS_TOKEN'], socket.gethostname(), os.environ['CRS_SECRET'])
    ticket = cli.assign_next_unassigned_for_state(ticket_type='encoding', to_state='encoding')
    if ticket is None:
        print('No Ticket for encoding')
        return

    print('Got Ticket for encoding:')
    print(ticket)

    print('Set Ticket done')
    cli.set_ticket_done(ticket)


if __name__ == '__main__':
    main()
