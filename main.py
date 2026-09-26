from services import (
    find_subject,
    find_topic,
    find_note,
    create_subject,
    create_topic,
    create_note,
    update_subject,
    update_topic,
    update_note,
    delete_subject,
    delete_topic,
    delete_note,
)

topic = update_topic("196340cd-f6cd-4a01-8d4a-ea81fcb5289b", "Piton")

print(topic.id)
print(topic.name)
print(topic.updated_at)