#!/usr/bin/env python
"""Helper script that uploads demultiplex (barcode) counts and QC data to godcs.
"""

import os
import sys
import argparse
from bcbio.solexa.flowcell import get_flowcell_info
from bcbio.pipeline.config_loader import load_config
from bcbio.google.sequencing_report import create_report_on_gdocs


def main():
	parser = argparse.ArgumentParser(description="(Re-)uploads google docs barcode and quality \
							metrics to google docs.")

	parser.add_argument("flowcell", type=str, help="The flowcell directory")
    	args = parser.parse_args()

	config = load_config(os.path.join(os.environ['HOME'], "config/post_process.yaml"))

	flowcell = os.path.basename(args.flowcell)
	
	fc_dir = os.path.join(config["analysis"]["store_dir"], flowcell)
	workdir = os.path.join(config["analysis"]["base_dir"], flowcell)

	fc_name, fc_date = get_flowcell_info(args.flowcell)
	run_info_file = os.path.join(fc_dir, "run_info.yaml")
	dir = {"work": workdir, "flowcell": fc_dir}

	create_report_on_gdocs(fc_date, fc_name, run_info_file, dir, config)


if __name__ == "__main__":
    main()
