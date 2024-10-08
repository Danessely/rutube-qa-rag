path_to_index = "init_data/flat.index"

path_to_excel = "init_data/qa_set.csv"

healthcheck_timeout = 30
healthcheck_sleep = 5
topn = 10

max_new_tokens = 512

popular_answers = {
    "popular_angry": "К сожалению, не могу ответить на вопрос. Пожалуйста, обратитесь в поддержку или попробуйте переформулировать свой запрос",
}

qr_prompt = \
"""
Тебе будет подана история общения пользователя и ассистента. Твоя задача - переписать запрос пользователя, учитывая историю диалога (контекстуализировать, чтобы его смысл был понятен вне остальных запросов).
Ты НЕ ДОЛЖЕН отвечать на вопрос! Твоя задача - ПЕРЕПИСАТЬ!
Если в истории только один запрос (от пользователя), оставь его как есть

===ИСТОРИЯ===
{history}

Ответь в формате JSON с единственным ключом "answer", значение которого и будет переписанный запрос. Отвечай только на русском, и очень кратко.
"""

stuff_prompt = \
"""
Тебе будет подан пользовательский запрос и релевантные фрагменты текста, в которых возможно содержится ответ на поставленный вопрос.
Проанализируй каждый фрагмент, и, если в нем есть ответ на вопрос пользователя, используй его для генерации финального ответа на изначальный пользовательский запрос.
Некоторые фрагменты могут быть помечены как не релевантные: игнорируй их.

ЗАПРОС: {query}
ФРАГМЕНТЫ ТЕКСТА:
{passages}

Ответь в формате JSON с единственным ключом "answer", значение которого и будет финальный ответ на вопрос с учетом поданного контекста. Отвечай только на русском.
"""

popularity_prompt = \
"""
Тебе будет подан пользовательский запрос, по которому нужно определить, хочет ли пользователь пользоваться чат-ботом.
Запрос: '{query}'.

Ответь в формате JSON с единственным ключом "answer", значение которого зависит от твоего решения:
1) Если пользователь задает вопрос не по теме работы с видеохостингом или на который нельзя ответить ([вернуть старый дизайн, бот тупой, как убрать бота, вернуться на старый портал, нужен оператор]), то значение ключа будет 'popular_angry';
2) Если все хорошо - 'ordinary'

Не пиши никаких пояснений к ответу! Ответ должен содержать только JSON словарь!
"""

domain_prompt = \
"""
Тебе будет подан пользовательский запрос, по которому нужно определить, относится он к видеохостингу Rutube (возможные темы: 'модерация', 'монетизация', 'управление аккаунтом', 'доступ к rutube', 'отсутствует', 'предложения', 'видео', 'трансляция', 'сотрудничество продвижение реклама', 'поиск', 'благотворительность донаты') или нет.
Запрос: '{query}'.

Ответь в формате JSON с единственным ключом "answer", значение которого зависит от твоего решения.
Если запрос ОТНОСИТСЯ к Rutube, то значение ключа будет равно "single". Примеры: ["как удалить видео?", "не получается зайти в кабинет", "как создать трансляцию?", "что такое rutube?", "как подключить монетизацию?"];
Если же запрос НЕ ОТНОСИТСЯ к технической поддержке видеохостинга (общие знания, неправильный, ошибочный, ругательный), то значение ключа будет "trash"
Не пиши никаких пояснений к ответу! Ответ должен содержать только JSON словарь!
"""

map_prompt = \
"""
Тебе будет подан пользовательский запрос и фрагмент текста, в котором возможно содержится ответ на заданный вопрос.
Проанализируй этот фрагмент, и, если в нем есть ответ на вопрос, используй его для генерации четкого и понятного ответа.
Если в фрагменте не содержится информации с помощью которой можно было бы ответить на поставленный вопрос, напиши в ответе "!не релевантный фрагмент!"

ЗАПРОС: {query}
ФРАГМЕНТ ТЕКСТА:
{passages}

Ответь в формате JSON с единственным ключом "answer", значение которого и будет ответом на вопрос с учетом поданного текста. Отвечай только на русском.
"""

def faiss_func(x):
    return f'Запрос: {x["question"]}; Ответ: {x["content"]}; Категория: {x["category"]}'
