import os
import argparse


def main():
    parser = argparse.ArgumentParser('Run a collection of test scripts/tools')
    parser.add_argument("-u", "--url", type=str, help="The target hostname")
    args = parser.parse_args()

    hostname = args.url

    # Format of scans [[NAME,EXECUTABLE,UPDATE COMMAND},...]
    scans = [["TestSSL", "/opt/testssl/testssl.sh " + hostname, "cd /opt/testssl;git pull"],
             ["Nikto", "nikto -h " + hostname, "nikto -update"],
             ["NMap Pt1", "nmap -n -v -O -sV -sC --reason -open " + hostname, None],
             ["NMap Pt2", "nmap -p http* --open -sC --script=http* " + hostname, None],
             ["CheckHeaders", "python /opt/checkHeaders/headers.py -u https://" + hostname, "cd /opt/checkHeaders;git pull"]
             ]

    for item in scans:
        print(item[0])
        if item[2] is not None:
            os.system(item[2])
        os.system(item[1])


if __name__ == "__main__":
    main()
