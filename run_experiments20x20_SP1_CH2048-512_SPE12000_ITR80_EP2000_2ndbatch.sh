#!/bin/bash

tarcs=(44 48 52 56 60)
for (( i=0; i<${#tarcs[@]}; i++ )); do
python -m spinup.run_simple \
    --algo ppo  \
    --env Flexibility20x20T"${tarcs[i]}"_SP1-v0 \
    --exp_name F20x20T"${tarcs[i]}"_SP1_PPO_CH2048-512_SPE12000_ITR80_EP2000  \
    --cpu 8 \
    --epochs 2000  \
    --steps_per_epoch 12000  \
    --save_freq 10  \
    --custom_h 2048-512 \
    --act tf.nn.relu  \
    --train_pi_iters 80  \
    --train_v_iters 80 \
    --do_checkpoint_eval; done
