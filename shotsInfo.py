"""
Name: Studio Desktop Client
Author :  Rajiv Sharma
Developer Website : www.hqvfx.com
Developer Email   : rajiv@hqvfx.com
Date Started : 16 sept 2018
Date Modified :
Description : Desktop client for Stdio Line Production pipeline

Download Application from : www.hqvfx.com/downloads
Source Code Website : www.github.com/hqvfx
Free Video Tutorials : www.youtube.com/vfxpipeline

Copyright (c) 2018, HQVFX(www.hqvfx.com) . All rights reserved.
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.

    * Redistributions in binary form must reproduce the above copyright
      notice, this list of conditions and the following disclaimer in the
      documentation and/or other materials provided with the distribution.

    * Neither the name of HQVFX(www.hqvfx.com) nor the names of any
      other contributors to this software may be used to endorse or
      promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""
import sys
import argparse
from PySide2 import QtWidgets

shots_info = {
    "sh001": {"status": "Completed", "assign_to": "Rajiv Sharma"},
    "sh002": {"status": "InProgress", "assign_to": "Sapna Sharma"},
    "sh003": {"status": "New", "assign_to": "Aayaan Sharma"}
}


def display_info(shot_id, query_key):
    app = QtWidgets.QApplication()
    shot = shots_info.get(shot_id, None)
    if shot:
        if query_key:
            info = shots_info[shot_id][query_key]
            data = "{} {} is {}".format(shot_id, query_key, info)
        else:
            data = "{} {} ".format(shot_id, shots_info[shot_id])
    else:
        data = "{} is not exist".format(shot_id)
    QtWidgets.QMessageBox.information(None, 'Shots Info Tool', data)

# display_info('sh003', 'status')

if __name__ == '__main__':
    # arg = sys.argv
    # display_info(arg[1], arg[2])
    parser =argparse.ArgumentParser(prog='Shot Info',
                                    usage='''
                                    Usage:
                                    Pass shots data in json format
                                    and this will rerun the value from the query key.
                                    ''',
                                    description='''
                                    -----------------------------------------------
                                    Description:
                                    This tool will display shots information
                                    -----------------------------------------------
                                    ''',
                                    epilog="Copyrights @ Rajiv Sharma (www.hqvfx.com)",
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    add_help=True
                                    )

    parser.add_argument("shot", type=str, help="Enter shot id. for example: sh001", metavar="SHOT LABEL ID")
    parser.add_argument("--key", "-k", type=str,
                        help="Optional: Enter query key for search information. for example: status", default='assign_to',
                        required=False)
    arg = parser.parse_args()
    display_info(arg.shot, arg.key)
