

from transformers import AutoTokenizer, AutoModel
tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True)
model = AutoModel.from_pretrained("THUDM/chatglm2-6b", trust_remote_code=True, device='cuda')
model = model.eval()
while True:
	input_text=input()
	response, history = model.chat(tokenizer, f"假设你是一个精通电力领域的工程师，擅长对于电力领域的问题给出高质量的回答。请根据可能有用的已知信息，分析题目，并总结你选择的答案是什么。已知信息:\nQuestion:{text}", history=[["假设你是一个精通电力领域的工程师，擅长对于电力领域的问题给出高质量的回答。请根据可能有用的已知信息，分析题目，并总结你选择的答案是什么。已知信息:根据欧姆定律，我们知道电压等于电流与电阻的乘积。\nQuestion:一个2欧姆的电阻，通过1A的电流，请问其两端的电压是多少？\nA:1V\nB:2V\nC:3V\nD:4V","分析:根据已知信息，我们知道电压是电流与电阻的乘积。所以，电阻两端的电压为2*1=2V.\n答案:A"]])
	print(response)
