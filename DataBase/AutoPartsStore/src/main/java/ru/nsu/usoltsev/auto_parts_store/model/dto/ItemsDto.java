package ru.nsu.usoltsev.auto_parts_store.model.dto;

import lombok.AllArgsConstructor;
import lombok.Data;
import ru.nsu.usoltsev.auto_parts_store.model.entity.Delivery;

import java.util.List;

@Data
@AllArgsConstructor
public class ItemsDto {
    private Long itemId;

    private String name;

    private String category;

    private Integer amount;

    private Integer defectAmount;

    private Integer price;

    private Integer cellNumber;

    private List<Delivery> deliveries;
}
