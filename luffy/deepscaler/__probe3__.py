```bash
# Clone the repository
git clone https://github.com/Dao-AILab/flash-attention/pull/824
```
- [ ] **luffy/verl/verl/models/llama.py:88** - ... requires the layout [batch_size, sequence_length, num_heads, head_dim].
- [ ] **x:1** - (zhangchi.usc1992): 1. support create. 2. Support init,
- [ ] **x:2** - pass *args and **kwargs is bug prone and not very convincing
- [ ] **a/b/c.py:3** - it seems that manual offload is slowly than FSDP offload
