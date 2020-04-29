#!/bin/bash

env_version=5
python -m spinup.run_flexibility \
    --algo ppo  \
    --env_name F10x10-v${env_version} \
    --exp_name F10x10_CH1024-128_ENV${env_version}  \
    --cpu 2 \
    --epochs 400  \
    --custom_h 1024-128 \
    --env_version ${env_version} \
    --env_input input_ran10x10a_cv0.8.pkl \
    --target_arcs  10 37 \
    --num_runs 4 \
    --save_freq 8  \
    --do_checkpoint_eval;
#done