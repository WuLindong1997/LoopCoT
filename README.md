# LoopCoT
运用双向的任务进行微调模型的一种方法，可以有效的提升主任务的表现。

## Main Result
    .
    ├── appreciation_result.png                                     mix data 与single data 的 appreciation 进行训练的比较图
    ├── generation_result.png                                       mix data 与single data 的 generation 进行训练的比较图
    ├── mean_ckpt_mix_appreciation.json                             mix data 训练的模型其中取最好的checkpoint循环20次evalution进行取平均appreciation的数据      (选择最好checkpoint，平均20次的结果)
    ├── mean_ckpt_mix_generation.json                               mix data 训练的模型其中取最好的checkpoint循环20次evalution进行取平均generation的数据        (选择最好checkpoint，平均20次的结果)
    ├── mean_ckpt_single_appreciation.json                          single data 训练的模型其中取最好的checkpoint循环20次evalution进行取平均appreciation的数据   (选择最好checkpoint，平均20次的结果)
    ├── mean_ckpt_single_generation.json                            single data 训练的模型其中取最好的checkpoint循环20次evalution进行取平均generation的数据     (选择最好checkpoint，平均20次的结果)
    ├── mix_data_all_evaluation.json                                mix data 训练的模型所有的checkpoint进行evalution的数据，其中测试数据为 generation 和 appreciation 的test数据之和
    ├── mix_data_appreciation_evaluation.json                       mix data 训练的模型所有的checkpoint进行evalution的数据，其中测试数据为 appreciation 的test数据
    ├── mix_data_generation_evaluation.json                         mix data 训练的模型所有的checkpoint进行evalution的数据，其中测试数据为 generation 的test数据
    ├── mix_summarize_keywords_appreciation_result.png              mix data 其中的generation数据进行了keywords和summatrize的数据和appreciation数据的之和训练出的模型checkpoint进行测评（数据最多的模型结果）
    ├── mix_summarize_keywords_data_appreciation_evaluation.json    mix data 其中的generation数据进行了keywords和summatrize的数据和appreciation数据的之和训练出的模型checkpoint进行测评（数据最多的模型结果）
    ├── mix_summarize_keywords_data_generation_evaluation.json      mix data 其中的generation数据进行了keywords和summatrize的数据和appreciation数据的之和训练出的模型checkpoint进行测评（数据最多的模型结果）
    ├── mix_summarize_keywords_generation_result.png                mix data 其中的generation数据进行了keywords和summatrize的数据和appreciation数据的之和训练出的模型checkpoint进行测评（数据最多的模型结果）
    ├── single_data_appreciation_evaluation.json                    single data 的模型所有checkpoint的evalution
    ├── single_data_generation_evaluation.json                      single data 的模型所有checkpoint的evalution
    ├──more_data_appreciation                                       数据最多的模型 appreciation 结果        (选择最好checkpoint，平均20次的结果)
    └──more_data_generation                                         数据最多的模型 generation 结果          (选择最好checkpoint，平均20次的结果)

    1. 结论
        混合数据的generation有所提升（mean_ckpt_mix_generation.json 和 mean_ckpt_single_generation.json）
        mean_ckpt_mix_generation.json
        {
            "rouge-1": 15.178094593495933,
            "rouge-2": 1.4220849390243904,
            "rouge-l": 11.96743788617886,
            "bleu-4": 7.207070365853658
        }
        mean_ckpt_single_generation
        {
            "rouge-1": 14.67471119918699,
            "rouge-2": 1.4612608333333335,
            "rouge-l": 11.434773760162601,
            "bleu-4": 6.598017215447155
        }

        最多数据的generation有所**（more_data_generation 和 mean_ckpt_single_generation.json）（可以说混合一半appreciation 的数据情况）

        more_data_generation(best result)
        {
            "rouge-1": 15.510993699186992,
            "rouge-2": 1.703537743902439,
            "rouge-l": 12.238842479674796,
            "bleu-4": 7.437776869918698
        }
        mean_ckpt_single_generation
        {
            "rouge-1": 14.67471119918699,
            "rouge-2": 1.4612608333333335,
            "rouge-l": 11.434773760162601,
            "bleu-4": 6.598017215447155
        }
