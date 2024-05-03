package ru.nsu.usoltsev.auto_parts_store.service;

import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import ru.nsu.usoltsev.auto_parts_store.exception.ResourceNotFoundException;
import ru.nsu.usoltsev.auto_parts_store.model.dto.ItemDto;
import ru.nsu.usoltsev.auto_parts_store.model.dto.querriesDto.ItemInfoDto;
import ru.nsu.usoltsev.auto_parts_store.model.entity.Item;
import ru.nsu.usoltsev.auto_parts_store.model.mapper.ItemMapper;
import ru.nsu.usoltsev.auto_parts_store.repository.ItemRepository;

import java.util.List;
import java.util.stream.Collectors;

@Service
public class ItemService {
    @Autowired
    private ItemRepository itemRepository;
    @Autowired
    private ObjectMapper objectMapper;

    public ItemDto saveItem(ItemDto itemDto) {
        Item customer = ItemMapper.INSTANCE.fromDto(itemDto);
        Item savedItem = itemRepository.saveAndFlush(customer);
        return ItemMapper.INSTANCE.toDto(savedItem);
    }

    public ItemDto getItemById(Long id) {
        return ItemMapper.INSTANCE.toDto(itemRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Item is not found by id: " + id)));
    }

    public List<ItemDto> getItems() {
        return itemRepository.findAll()
                .stream()
                .map(ItemMapper.INSTANCE::toDto)
                .collect(Collectors.toList());
    }

    public List<ItemInfoDto> getItemsInfo() {
        return itemRepository.findAllItemsInfo()
                .stream()
                .map(row -> new ItemInfoDto(
                        (String) row[0],
                        (Integer) row[1],
                        (Integer) row[2]
                ))
                .collect(Collectors.toList());
    }

    public List<ItemDto> getItemsByCategory(String category) {
        return itemRepository.findByCategory(category)
                .stream()
                .map(ItemMapper.INSTANCE::toDto)
                .collect(Collectors.toList());
    }

    public List<String> getTopTen() {
        return itemRepository.getTopTenSoldDetails()
                .stream()
                .map(a -> {
                    try {
                        return objectMapper.writeValueAsString(a);
                    } catch (JsonProcessingException e) {
                        throw new RuntimeException(e);
                    }
                })
                .collect(Collectors.toList());
    }

}