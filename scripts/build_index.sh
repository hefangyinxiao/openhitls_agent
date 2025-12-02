source .env
# generate graph index for SWE-bench_Lite
python src/dependency_graph/batch_build_graph.py \
    --repo_path ${REPO_PATH} \
    --index_dir ${INDEX_PATH} \
    --num_processes 10

python src/repo_index/build_bm25_index.py \
    --repo_path ${REPO_PATH} \
    --index_dir ${INDEX_PATH} \
    --num_processes 10