# openAI-project

## installation
pip install openai

## Set openAI Env variab
export OPENAI_API_KEY="<OPENAI_API_KEY>"

## CLI data preperation tool
openai tools fine_tunes.prepare_data -f <LOCAL_FILE>

## Tokens

### Adams privata
- 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

### Cost for output.jsonl (Davinci)
(Ctrl-C will interrupt the stream, but not cancel the fine-tune)
[2022-12-31 14:33:25] Created fine-tune: ft-xwUx46BbyRe8vfQx6PUQepry
[2022-12-31 14:34:46] Fine-tune costs $0.04
[2022-12-31 14:34:46] Fine-tune enqueued. Queue number: 0
[2022-12-31 14:34:48] Fine-tune started

### What have been done
1. converted txt to json
2. Ran CLI data preperation tool (Confirms data is correct and gives advice)
3. Ran training command
4. (Error The majority of examples in the training file contain more than the 2048 tokens allowed for this model.)
5. Small program making sentencens
6. openai api fine_tunes.create -t ./data/output.jsonl -m davinci


